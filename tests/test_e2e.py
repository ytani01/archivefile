# -*- coding: utf-8 -*-
# end-to-end test: archivefile command

import os
import shutil
import subprocess

import pytest


@pytest.fixture
def setup_test_environment(tmp_path):
    """テスト環境のセットアップ"""
    # 一時的なソースファイルを作成
    src_file_content = "これはテストファイルです。"
    src_file_name = "test_file.txt"
    src_file_path = tmp_path / src_file_name
    src_file_path.write_text(src_file_content)

    # 一時的なアーカイブディレクトリを作成
    archives_dir = tmp_path / "archives"
    archives_dir.mkdir()

    # テスト関数にパス、ディレクトリ、コンテンツを渡す
    yield src_file_path, archives_dir, src_file_content

    # クリーンアップ
    if os.path.exists(tmp_path):
        shutil.rmtree(tmp_path)


def test_archive_single_file_default_options(setup_test_environment):
    """単一ファイルをデフォルトオプションでアーカイブするテスト"""
    src_file_path, archives_dir, src_file_content = setup_test_environment
    src_file_name = src_file_path.name
    src_file_basename, _ = os.path.splitext(src_file_name)

    # コマンドを実行
    command = [
        "archivefile",
        str(src_file_path),
        "--dstdir",
        str(archives_dir),
        "--debug",  # デバッグ出力を有効にする
    ]
    result = subprocess.run(
        command, capture_output=True, text=True, check=False
    )

    # アサーション
    assert result.returncode == 0
    assert "finish" in result.stderr

    # ソースファイルが移動されたことを確認
    assert not src_file_path.exists()

    archived_files = list(archives_dir.iterdir())
    assert len(archived_files) == 1  # ファイルが1つだけ

    archived_file_path = archived_files[0]
    assert archived_file_path.name.startswith("20")
    assert archived_file_path.name.endswith("-done.txt")
    assert f"-{src_file_basename}-done.txt" in archived_file_path.name

    # コンテンツが正しいことを確認
    assert archived_file_path.read_text() == src_file_content


def test_archive_multiple_files_custom_options(tmp_path):
    """複数ファイルをカスタムオプションでアーカイブするテスト"""
    # 複数の仮のソースファイルを作成
    src_file_content1 = "ファイル1の内容。"
    src_file_name1 = "doc1.txt"
    src_file_path1 = tmp_path / src_file_name1
    src_file_path1.write_text(src_file_content1)

    src_file_content2 = "ファイル2の内容。"
    src_file_name2 = "report.pdf"
    src_file_path2 = tmp_path / src_file_name2
    src_file_path2.write_text(src_file_content2)

    # カスタムステータスと保存先ディレクトリを定義
    custom_stat = "processed"
    custom_dstdir = tmp_path / "my_custom_archives"
    custom_dstdir.mkdir()

    # コマンドを実行
    command = [
        "archivefile",
        str(src_file_path1),
        str(src_file_path2),
        "--stat",
        custom_stat,
        "--dstdir",
        str(custom_dstdir),
        "--debug",
    ]
    result = subprocess.run(
        command, capture_output=True, text=True, check=False
    )

    # アサーション
    assert result.returncode == 0
    assert "finish" in result.stderr

    # ソースファイルが移動されたことを確認
    assert not src_file_path1.exists()
    assert not src_file_path2.exists()

    # アーカイブされたファイルが存在し、正しくリネームされていることを確認
    archived_files = list(custom_dstdir.iterdir())
    assert len(archived_files) == 2

    # ファイル1の確認
    src_file_basename1, src_file_ext1 = os.path.splitext(src_file_name1)
    archived_file_path1 = next(
        f for f in archived_files if src_file_basename1 in f.name
    )
    assert archived_file_path1.name.startswith("20")
    assert archived_file_path1.name.endswith(f"-{custom_stat}{src_file_ext1}")
    assert (
        f"-{src_file_basename1}-{custom_stat}{src_file_ext1}"
        in archived_file_path1.name
    )
    assert archived_file_path1.read_text() == src_file_content1

    # ファイル2の確認
    src_file_basename2, src_file_ext2 = os.path.splitext(src_file_name2)
    archived_file_path2 = next(
        f for f in archived_files if src_file_basename2 in f.name
    )
    assert archived_file_path2.name.startswith("20")
    assert archived_file_path2.name.endswith(f"-{custom_stat}{src_file_ext2}")
    assert (
        f"-{src_file_basename2}-{custom_stat}{src_file_ext2}"
        in archived_file_path2.name
    )
    assert archived_file_path2.read_text() == src_file_content2

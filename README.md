# archivefile

`archivefile`は、指定されたファイルをアーカイブディレクトリに移動し、リネームするためのコマンドラインユーティリティです。

## == 概要

このツールは、ファイルを整理し、タイムスタンプとステータス情報を含む新しいファイル名でアーカイブするのに役立ちます。


## == 機能

-   指定されたファイルをアーカイブディレクトリに移動します。
-   ファイル名にタイムスタンプ（`YYYYMMDD-HHMMSS`）とステータス（例: `done`）を付加してリネームします。


## == インストール

このプロジェクトはPython 3.13以上を必要とします。

```bash
# リポジトリをクローン
git clone https://github.com/your-repo/archivefile.git
cd archivefile

# 依存関係をインストール (uvを使用する場合)
uv pip install .

# 通常のシェル環境で使えるようにする(~/.local/bin にインストール)
uv tool install .
```

## == 使用方法

`archivefile`コマンドは、アーカイブしたいファイルとオプションの引数を取ります。

```bash
archivefile <ソースファイル...> [オプション]
```

### == 引数

-   `<ソースファイル...>`: アーカイブする1つ以上のファイルパス。


### === オプション

-   `-s`, `--stat <ステータス>`: ファイル名に付加するステータス文字列。デフォルトは `done` です。
-   `-d`, `--dstdir <ディレクトリ>`: アーカイブファイルを保存するディレクトリ。デフォルトは `./archives` です。
-   `-v`, `--verbose`: 詳細な出力を表示します。


### === 例

1.  `my_document.txt` をデフォルトのアーカイブディレクトリに移動し、`done` ステータスでリネームします。
    ```bash
    archivefile my_document.txt
    ```
    (例: `archives/20250928-103000-my_document-done.txt` のようにリネームされます)

2.  複数のファイルを `processed` ステータスで `/tmp/archived` ディレクトリに移動します。
    ```bash
    archivefile report.pdf image.jpg --stat processed --dstdir /tmp/archived
    ```


## == 開発

### Linting

```basha
ruff check .
flake8
```

### Formatting

```bash
ruff format .
isort .
```

### Type Checking

```bash
mypy .
pyright
```

### Testing

```bash
pytest
```

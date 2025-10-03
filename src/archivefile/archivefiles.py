#
# (c) 2025 Yoichi Tanibayashi
#
import datetime
import os
import sys

from pyclickutils import errmsg, get_logger


class ArchiveFiles:
    """Archive files"""

    def __init__(self, srcfiles, stat, dstdir, verbose_flag, debug):
        """constractor"""
        self.__debug = debug
        self.__log = get_logger(__class__.__name__, self.__debug)
        self.__log.debug(
            "srcfiles=%s, stat=%s, dstdir=%s, verbose_flag=%s",
            srcfiles,
            stat,
            dstdir,
            verbose_flag,
        )

        self.srcfiles = srcfiles
        self.stat = stat
        self.dstdir = dstdir
        self.verbose_flag = verbose_flag

    def archive_files(self):
        """Archive files"""
        self.__log.debug("")

        # dstdirnoの存在確認
        if not os.path.exists(self.dstdir):
            self.__log.error("directory not found: %s/", self.dstdir)
            sys.exit(2)

        _results = []
        for _f in self.srcfiles:
            _r = self.archive_one_file(_f)
            _results.append(_r)

        self.__log.debug("results=%s", _results)
        if sum(_results) > 0:
            sys.exit(max(_results))

    def archive_one_file(self, src_file) -> int:
        """Archive one file"""
        self.__log.debug("")

        # ファイルの存在確認
        if not os.path.exists(src_file):
            self.__log.error("file not found: %a", src_file)
            return 1

        # ファイル名と拡張子を分割
        base_name = os.path.basename(src_file)
        file_root, file_ext = os.path.splitext(base_name)
        self.__log.debug(
            "base_name:%a, file_root:%a, file_ext:%a",
            base_name,
            file_root,
            file_ext,
        )

        # タイムスタンプを付加
        current_time = datetime.datetime.now()
        timestamp = current_time.strftime("%Y%m%d-%H%M%S")
        new_filename = f"{timestamp}-{file_root}-{self.stat}{file_ext}"
        self.__log.debug("new_filename: %a", new_filename)

        # 新しいパスを生成
        new_path = os.path.join(self.dstdir, new_filename)
        self.__log.debug("new_path: %a", new_path)

        try:
            os.rename(src_file, new_path)
            if self.verbose_flag:
                print(f"{src_file} ==> {new_path}")
        except OSError as _e:
            self.__log.error(errmsg(_e))
            return 3

        return 0

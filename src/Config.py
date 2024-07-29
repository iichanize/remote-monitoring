from dynaconf import Dynaconf

settings = Dynaconf(
    settings_files=['../config.json'], # 設定ファイルの場所を指定
)

inputPath1 = settings.inputPath1
inputPath2 = settings.inputPath2
outputDir = settings.outputDir

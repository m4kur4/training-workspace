# 第一引数に種別、第二引数にモジュール名を指定して所定構成のフォルダを生成する
# 既に同名フォルダが存在する場合は何もしない

# TODO: 引数チェック
# TODO: ファイル存在チェック

mkdir -p $1
mkdir -p $1/$2
mkdir -p $1/$2/src
mkdir -p $1/$2/test
mkdir -p $1/$2/archive
touch -p $1/$2/README.md


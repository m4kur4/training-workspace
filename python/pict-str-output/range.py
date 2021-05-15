import argparse

def get_num_range_str(start: int, end: int) -> str:
    """指定した開始／終了までの数値を'|'区切りの文字列にして返却する
        Args:
            start (int): 先頭の数値
            end (int): 末尾の数値
        Return:
            結果文字列
    """
    if end < start:
        return '先頭と末尾の大小関係が不正です'

    result = ''
    for i in range(start, end + 1):
        result += str(i)
        if i != end:
            result += '|'
    return result


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('start')
    parser.add_argument('end')
    args = parser.parse_args()

    start = int(args.start)
    end = int(args.end)
    output = get_num_range_str(start, end)
    print(output)

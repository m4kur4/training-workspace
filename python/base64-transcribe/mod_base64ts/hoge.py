import sys
import json

BYTE_SIZE = 8

def str_to_bin(s):
	"""文字列sをバイナリの文字列へ変換する"""
	bin_str = ''
	# ord関数で文字をASCIIコードへ変換し、シフト演算で各桁のビットを取り出す
	for c in s:
		for i in range(BYTE_SIZE):
			bin_str += str((ord(c) >> (BYTE_SIZE - (i + 1))) & 1)
	return bin_str


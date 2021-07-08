import numpy as np


# 関数の宣言
def matrix_product_calculator(matrix_1, matrix_2):
	"""
	function : 行列1[matrix_1]と行列2[matrix_2]の行列積[matrix_product]を返す関数

	:param matrix_1: array
		行列1
	:param matrix_2: array
		行列2

	count : int (計算用)
		計算結果格納用
	list_of_matrix_12 : list (格納用)
		計算結果を配列に変える前に保存しておくリスト

	:return: matrix_product: array
		行列1と行列2の行列積
	"""

	# 初期値の設定
	count = 0
	list_of_matrix_12 = []
	# 計算
	for i in range(matrix_1.shape[0]):
		for j in range(matrix_2.shape[1]):
			# ここのrangeはmatrix_2.shape[0]でも可能(同じ値をとる)
			for k in range(matrix_1.shape[1]):
				count += matrix_1[i][k] * matrix_2[k][j]
			# 結果の保存
			list_of_matrix_12.append(count)
			# 値のリセット
			count = 0

	# リストをarrayに変換、積の形にreshape
	matrix_product = np.array(list_of_matrix_12).reshape(matrix_1.shape[0], matrix_2.shape[1])
	# 返り値の設定
	return matrix_product

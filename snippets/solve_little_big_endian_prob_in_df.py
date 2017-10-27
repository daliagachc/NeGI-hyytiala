# project name: autumn_school_2017_hyyutiala
# created by diego aliaga daliaga_at_chacaltaya.edu.bo

def solve_little_big_endian_prob_in_df(df_list):
	#this function solves the cryptic error regarding little endian and big endian
	# the problem occurs when you mix dtypes in the dataframes
	#the function does not return anything as the dtype transformation is stored in the original dataframe
	#lets loop through the dataframes in df_list
	for i in range(len(df_list)):
		#lets loop through each column in the dataframe
		for col in df_list[i]:
			#lets store the type of the column dataframe
			dty=df_list[i][col].dtype
			#if the type is '>f8' (big endian) lets convert it to little endian(f8)
			if dty =='>f8':
				df_list[i][col]=df_list[i][col].astype('f8')

#example:
# define a list with the dataframe that you want to be fixed
#   df_list[df1,df2,...]
#run the funct on the list
#   solve_little_big_endian_prob_in_df(df_list)

# Nama  : Nadia Nazila Ramadina
# NIM   : 20051397028
# Praktikum 1 Grafika Komputer

def bresenham(x1,y1,x2, y2):

	m_new = 2 * (y2 - y1)
	slope_error_new = m_new - (x2 - x1)

	y=y1
	for x in range(x1,x2+1):
	
		print("(",x ,",",y ,")\n")

		slope_error_new =slope_error_new + m_new

		
		if (slope_error_new >= 0):
			y=y+1
			slope_error_new =slope_error_new - 2 * (x2 - x1)
		
	


if __name__=='__main__':
	x1 = -3
	y1 = 3
	x2 = -1
	y2 = -3
	bresenham(x1, y1, x2, y2)



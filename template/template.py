import pygame

class Pipe():
	def __init__(self,screen,y=0,x=512):
		# 图片
		pipeUpImageName = './img/pipe_down.png'
		pipeDownImageName = './img/pipe_up.png'

		# 导入图片
		self.image_up = pygame.image.load(pipeUpImageName)
		self.image_down = pygame.image.load(pipeDownImageName)

		# 图片大小
		self.image_width = 52
		self.image_height = 320

		# 图片位置
		self.x_up = x
		self.y_up = y
		self.x_down = x
		self.y_down = y + 400

		#获取主屏幕的surface对象
		self.window = screen

	def getPos(self):
		return [[self.x_up, self.y_up, self.image_width,
	 	self.image_height],[self.x_down, self.y_down,
		self.image_width, self.image_height]]

	# 检测是否出界
	def checkOut(self):
		if self.x_up <= -52:
			return True
		else:
			return False
	#设置pipe向左移动方法
	def move(self):
		self.x_up -= 1.5
		self.x_down -= 1.5
	#绘制pipe
	def draw(self):
		self.window.blit(self.image_up, (self.x_up, self.y_up))
		self.window.blit(self.image_down, (self.x_down, self.y_down))


class Bird():
	"""这是一个鸟的原型类"""
	def __init__(self, screen):

		# 鸟图片路径
		bird_img = './img/bird1_1.png'
		# 导入鸟图片surface对象
		self.image = pygame.image.load(bird_img)

		# 图片大小
		self.image_width = 48
		self.image_height = 48

		# 设置默认坐标
		self.x = 0
		self.y = 208

		self.window = screen

		# 判断鸟是否是在上升状态
		self.isjump = False

	#获取鸟的位置
	def getPos(self):
		return [self.x, self.y, self.image_width, self.image_height]

	#正常状态下鸟的图片
	def normal(self):
		#鸟在上升状态下的图片路径
		jumpImageName = './img/bird1_1.png'
		# 生成surfac对象
		self.image = pygame.image.load(jumpImageName)

	#改变鸟的状态
	def jump(self):
		self.isjump = True
		
	# 上移
	def moveUp(self):
		# 图片路径
		jumpImageName = './img/bird1_0.png'
		# 生成surfac对象
		self.image = pygame.image.load(jumpImageName)
		if self.y <= 0:
			self.y = 0
		else:
			self.y -= 5

	# 下移
	def moveDown(self):
		self.y += 2
   
	# 绘制图形
	def draw(self):
		self.window.blit(self.image, (self.x, self.y))

	# 按键操作处理
	def keyHandle(self, keyValue):
		if keyValue == 'space':
			self.moveUp()
		
		
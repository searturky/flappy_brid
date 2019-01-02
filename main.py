import sys,pygame,time,random
sys.path.append('./template')
from template import *
from pygame.locals import *

if __name__ == '__main__':
	pygame.init()#加载pygame模块使初始化
	fclock = pygame.time.Clock()
	pygame.display.set_caption('fb')	#取窗口名
	screen_size = 288,512 	#窗口大小
	screen = pygame.display.set_mode(screen_size) 	#窗口,获取surface对象
	background = pygame.image.load('./img/bg_night.png')#加载背景图片
	screen.blit(background, (0, 0))#添加背景图像进入窗口
	font = pygame.font.SysFont(None, 40)#设置字体格式
	#这是一个加载主界面的方法
	def load(screen,background):
		player = Bird(screen)#获取鸟的实例对象
		player.draw()#绘制鸟
		running_control = True#显示游戏是否正在运行
		pipeList = []#存放pipe的实例，可以统一处理和释放
		pipe_frequency = 0#控制pipe的生成频率
		score = 0#分数

		while running_control:
			screen.blit(background, (0, 0))#添加背景图像进入窗口
			player.draw()#显示鸟图片

			if pipe_frequency % 120 == 0:
				num = random.randint(-208, 0)
				pipe = Pipe(screen, num)
				pipeList.append(pipe)

			pipe_frequency += 1

			if pipe_frequency >= 240:
				pipe_frequency = 0

			if player.isjump == True:
				player.moveUp()

			player.moveDown()

			if player.y >= 512 :
				running_control = False

			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key == K_SPACE:
						player.keyHandle('space')
						player.jump()
			#print(event)
				if event.type == pygame.KEYUP:
					if event.key == K_SPACE:
						player.isjump = False
						player.normal()
				if event.type == pygame.QUIT:
					exit()

			for pipe in pipeList:
				pipe.move()
				if pipe.checkOut():
				 	pipeList.remove(pipe)
				 	score += 1

				l = pipe.getPos()
				x1,y1,w1,h1 = player.getPos()
				x2,y2,w2,h2 = l[0]
				x3,y3,w3,h3 = l[1]

				if (y1 + h1 // 2) >= y3 and (y1 + h1 // 2) <= (y3 + h3):
					if x3 <= (x1 + w1):
						running_control = False
						break
			
				if (y1 + h1 // 2) >= y2 and (y1 + h1 // 2) <= (y2 + h2):
					if x2 <= (x1 + w1):
						running_control = False
						break	
		
			for pipe in pipeList:	
				pipe.draw()

			text_fmt = font.render(str(score), 1, (255,255,255))#初始化字体
			screen.blit(text_fmt, (0,0))
			pygame.display.update()#实时更新窗口
			fclock.tick(60)#设置帧率为60
		#time.sleep(0.03)
	
		re_load = True#控制是否再开一局
		while re_load:
			# 读出背景图片
			background = pygame.image.load('./img/text_game_over.png').convert()
			screen.blit(background, (42, 200))
			pygame.display.update()#更新画面
			for event in pygame.event.get():
				if event.type == pygame.MOUSEBUTTONDOWN:
					re_load = False
				if event.type == pygame.QUIT:
			 		exit()

	while True:
		load(screen,background)
		for event in pygame.event.get():
				if event.type == pygame.QUIT:
					exit()
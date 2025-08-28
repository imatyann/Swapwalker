import pygame

import game.settings as settings
import game.player as player
import game.camera as camera

def start():
    """起動時に実行される関数"""

    # pygame初期設定
    pygame.init()
    screen_width = settings.SCREEN_WIDTH
    screen_height = settings.SCREEN_HEIGHT
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("スワップウォーカー")
    clock = pygame.time.Clock()

    # 盤面初期設定
    state = "playing"
    center_pos = (screen_width/2,screen_height/2)

    # カメラ初期設定
    main_camera = camera.Camera(
        settings.CAMERA_FIRST_X,
        settings.CAMERA_FIRST_Y
    )

    # 操作キャラ初期設定
    main_player = player.Player(
        (255,255,255),
        50,
        settings.G,
        0,
        False
    )
    main_player.reset_fall()

    running = True
    while running:
        if state == "playing":
            now = pygame.time.get_ticks()

            # 背景の描画
            screen.fill(settings.BG_COLOR)

            # 入力受付
            for event in pygame.event.get():
                # ウィンドウの終了
                if event.type == pygame.QUIT:
                    running = False
                
                # 操作受付
                if event.type == pygame.KEYDOWN:
                    main_player.reset_fall()
                    main_player.y = 0
            
            #主人公に関する処理
            main_player.fall()
            
            # オブジェクト描画
            main_player.draw(screen,main_camera.x,main_camera.y,center_pos)

            # 画面更新
            pygame.display.flip()
            clock.tick(settings.FPS)




        else:
            pass
         
    
    pygame.quit()
    


if __name__ == "__main__":
    start()

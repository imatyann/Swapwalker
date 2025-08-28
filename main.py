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

    # カメラ初期設定
    main_camera = camera.Camera(
        settings.CAMERA_FIRST_X,
        settings.CAMERA_FIRST_Y
    )

    # 盤面初期設定
    state = "playing"
    center_pos = (screen_width/2,screen_height/2)
    ground_y = screen_height - settings.GROUND_Y 



    # 操作キャラ初期設定
    main_player = player.Player(
        settings.PLAYER_COLOR,
        settings.PLAYER_FIRST_X,
        settings.PLAYER_FIRST_Y,
        settings.G,
        0,
        False,
        settings.PLAYER_RADIUS
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
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        state = "reset"

            # 操作受付    
            keys = pygame.key.get_pressed()

            if keys[pygame.K_SPACE]:
                main_player.reset_fall()
                main_player.y = 0
            elif keys[pygame.K_d]:
                main_camera.move_x(5)
            elif keys[pygame.K_a]:
                main_camera.move_x(-5)

            #主人公に関する処理
            if ground_y > main_player.y:
                main_player.on_ground = False
            else:
                main_player.on_ground = True
            main_player.fall()

            
            # オブジェクト描画
            main_player.draw(screen,main_camera.x,main_camera.y,center_pos)

            # 画面更新
            pygame.display.flip()
            clock.tick(settings.FPS)

        else:
            # 入力受付
            for event in pygame.event.get():
                # ウィンドウの終了
                if event.type == pygame.QUIT:
                    running = False

         
    
    pygame.quit()
    


if __name__ == "__main__":
    start()

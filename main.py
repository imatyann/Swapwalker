import pygame

import game.settings as settings
import game.player as player
import game.camera as camera
import game.goal as goal
import game.reticle as reticle

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
    ground_y = screen_height - settings.GROUND_Y 

    main_camera,state,main_goal,main_player,main_reticle = reset_all()

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
                        main_camera,state,main_goal,main_player,main_reticle = reset_all()


            # 操作受付    
            keys = pygame.key.get_pressed()

            if keys[pygame.K_SPACE]:
                main_player.reset_fall()
                main_player.y = 0
            elif keys[pygame.K_d]:
                main_camera.move_x(5)
                main_player.move_x(5)
            elif keys[pygame.K_a]:
                main_camera.move_x(-5)
                main_player.move_x(-5)
            elif keys[pygame.K_b]:
                print(main_player.x,main_player.y)

            # 主人公に関する処理
            # 足場判定
            if ground_y > main_player.y + main_player.radius:
                main_player.on_ground = False
            else:
                main_player.on_ground = True
            main_player.fall()

            # 照準設定 
            mouse_pos = pygame.mouse.get_pos()
            dx, dy = mouse_pos[0] - main_player.x, mouse_pos[1] - main_player.y 
            half_line_pos = (1000 * dx + main_player.x, 1000 * dy + main_player.y)

            # オブジェクト描画
            main_reticle.draw(screen,(main_player.x,main_player.y),half_line_pos)
            main_player.draw(screen,main_camera.x,main_camera.y,center_pos)
            main_goal.draw(screen,main_camera.x,main_camera.y)

        

            # ゴール判定
            if main_goal.is_touch_object(main_player.x,main_player.y):
                state = "goal"
                goal_event(screen)

            

            # 画面更新
            pygame.display.flip()
            clock.tick(settings.FPS)

        else:
            # 入力受付
            for event in pygame.event.get():
                # ウィンドウの終了
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if state in {"gameover","goal"}:
                        if event.key == pygame.K_r:
                            main_camera,state,main_goal,main_player,main_reticle = reset_all()
                            

         
    
    pygame.quit()
    
def goal_event(screen):
    """ゴール時の演出"""
    font = pygame.font.Font(None, settings.CLEAR_FONT_SIZE)
    text = font.render("GAME CLEAR", True, settings.CLEAR_FONT_COLOR)
    text_rect = text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))

    screen.blit(text, text_rect)

def reset_all():
    """全てリセットし初期設定に戻す関数"""
    # カメラ初期設定
    main_camera = camera.Camera(
        settings.CAMERA_FIRST_X,
        settings.CAMERA_FIRST_Y
    )

    # 盤面初期設定
    state = "playing"

    # 盤面オブジェクト初期設定
    main_goal = goal.Goal(
        settings.GOAL_X,
        settings.GOAL_Y,
        settings.GOAL_COLOR,
        settings.GOAL_WIDTH,
        settings.GOAL_HEIGHT
    )

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

    # レティクル初期設定
    main_reticle = reticle.Reticle(
        1,
        (0,0,0)
    )

    return main_camera,state,main_goal,main_player,main_reticle


if __name__ == "__main__":
    start()

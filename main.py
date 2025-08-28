import pygame

import game.settings as settings
import game.player as player


def start():
    """起動時に実行される関数"""

    # pygame初期設定
    pygame.init()
    screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
    pygame.display.set_caption("スワップウォーカー")
    clock = pygame.time.Clock()

    # 操作キャラ初期設定
    player = player.Player(
        (255,255,255)
    )

    running = True
    while running:
        now = pygame.time.get_ticks()

        # 背景の描画
        screen.fill(settings.BG_COLOR)

        # 入力受付
        for event in pygame.event.get():
            # ウィンドウの終了
            if event.type == pygame.QUIT:
                running = False
            

        # 画面更新
        pygame.display.flip()
        clock.tick(settings.FPS)
    
    pygame.quit()
    


if __name__ == "__main__":
    start()

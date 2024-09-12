if __name__ == '__main__':

    import pygame
    import sys

    # Pygame 초기화
    pygame.init()

    # 화면 크기 설정
    screen_width, screen_height = 400, 700


    screen = pygame.display.set_mode((screen_width, screen_height))

    # 창 제목 설정
    pygame.display.set_caption("Bowling Game")

    # 색상 정의
    white = (255, 255, 255)

    # 메인 루프
    while True:
        # 이벤트 루프
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # 창 닫기 이벤트 처리
                pygame.quit()
                sys.exit()

        # 화면 채우기
        screen.fill(white)

        # 화면 업데이트
        pygame.display.flip()

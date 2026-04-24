from src.greeting import print_greeting, print_farewell


def test_greeting():
    # 이 테스트는 실습 2에서 충돌 해결 후 통과해야 합니다
    # 충돌 해결 후 print_greeting의 동작에 맞게 수정하세요
    pass


def test_farewell():
    assert print_farewell("World") is not None

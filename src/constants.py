#
WIDTH, HEIGHT = 1920, 1080
TITLE = "Matrix Rain"
FPS = 60

NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

ALPHABET = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V', 'W', 'X', 'Y', 'Z']

KATAKANA = ['ァ','ア','ィ','イ','ゥ','ウ','ェ','エ','ォ','オ','カ','ガ','キ','ギ','ク','グ','ケ','ゲ','コ','ゴ','サ','ザ',
            'シ','ジ','ス','ズ','セ','ゼ','ソ','ゾ','タ','ダ','チ','ヂ','ッ','ツ','ヅ','テ','デ','ト','ド','ナ','ニ','ヌ',
            'ネ','ノ','ハ','バ','パ','ヒ','ビ','ピ','フ','ブ','プ','ヘ','ベ','ペ','ホ','ボ','ポ','マ','ミ','ム','メ','モ',
            'ャ','ヤ','ュ','ユ','ョ','ヨ','ラ','リ','ル','レ','ロ','ヮ','ワ','ヰ','ヱ','ヲ','ン','ヴ','ヵ','ヶ','ヷ','ヸ',
            'ヹ','ヺ','・']

HIRAGANA = ['ぁ','あ','ぃ','い','ぅ','う','ぇ','え','ぉ','お','か','が','き','ぎ','く','ぐ','け','げ','こ','ご','さ','ざ',
            'し', 'じ','す','ず','せ','ぜ','そ','ぞ','た','だ','ち','ぢ','っ','つ','づ','て','で','と','ど','な','に','ぬ',
            'ね','の', 'は','ば','ぱ','ひ','び','ぴ','ふ','ぶ','ぷ','へ','べ','ぺ','ほ','ぼ','ぽ','ま','み','む','め','も',
            'ゃ','や','ゅ', 'ゆ','ょ','よ','ら','り','る','れ','ろ','ゎ','わ','ゐ','ゑ','を','ん','ゔ']

ALLOWED_LETTERS = NUMBERS + ALPHABET + KATAKANA + HIRAGANA

FONT_NAME = 'MS Gothic'
MIN_FONT_SIZE = 10
MAX_FONT_SIZE = 100
PADDING = 5

MIN_LETTER_TIME = 1000
MAX_LETTER_TIME = 1500
SPEED_MULT = 0.2
MAX_TRAILS = 150

GREENISH_WHITE = (217, 255, 217, 255)  # pygame.Color('green').lerp((255, 255, 255), 0.85)
GREEN = (0, 255, 0, 255)  # pygame.Color('green')
BLACK = (0, 0, 0)

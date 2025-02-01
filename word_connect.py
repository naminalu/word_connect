import sys

class WordConnect:
    def __init__(self, file):
        # 単語の辞書
        self.dic = {}
        # 連結する単語の最大数(戦闘を除いて)
        self.max_word_num = 0

        with open(file, encoding='utf8') as f:
            data = f.readlines()

        max_num = 0
        for d in data:
            p = d.rstrip().split(' ')
            k = p[0]
            if k not in self.dic:
                self.dic[k] = []
            self.dic[k].append(p[1:])
            if len(p[1:]) > max_num:
                max_num = len(p[1:])
        self.max_word_num = max_num
   
    def conver_str(self, line: str) -> str:
        words = line.split(' ')
        # 処理を簡単にするために、空文字の配列を追加する.
        words.extend(['' for n in range(self.max_word_num)])

        while True:
            l = len(words)
            self.convert_list(words)
            if l == len(words):
                line = ' '.join(words)
                break
        return line

    def convert_list(self, words: list[str]):
        for i, word in enumerate(words):
            if word == '':
                break
            # 辞書に単語がなければ、次の単語へうつる.
            if word not in self.dic:
                continue

            for j, tmp in enumerate(self.dic[word]):
                # 連結対象の単語がすべて一致するかチェックする.
                for p in tmp:
                    if p != words[i + 1 + j]:
                        break
                else:
                    # 文字列を連結、不要になった要素を削除する.
                    words[i] = word + ''.join(tmp)
                    del words[i+1:i+1+len(tmp)]
                    return

def main() -> int:
    w = WordConnect(sys.argv[1])

    with open(sys.argv[2], encoding='utf8') as f:
        data = f.readlines()
    data = [d.rstrip() for d in data]

    for d in data:
        l = w.conver_str(d.rstrip())
        print(l)

    pass

    return 0

if __name__ == '__main__':
    sys.exit(main())

phrase = "The right format"

if len(phrase) > 42:
    print(phrase[0:41])
    exit()
while len(phrase) != 42:
    phrase = "-" + phrase

print(phrase, end = "")

## | cat -e 했을 때, $와 %의 차이
## %는 끝났다는 뜻, $는 줄바꿈의 뜻?
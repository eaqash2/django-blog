import re


class ReverseRussianWordsMiddleware:
    count = 1

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if (
            ReverseRussianWordsMiddleware.count % 10 == 0
        ):
            response.content = self.reverse_russian_words(
                response.content.decode("utf-8"),
            )
        ReverseRussianWordsMiddleware.count += 1

        return response

    def reverse_russian_words(self, content):
        regular = re.compile(r"\b[a-zA-Z]+\b")
        content = regular.sub(lambda w: w.group()[::-1], content)
        return content.encode("utf-8")


__all__ = []
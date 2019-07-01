# django-category-filter

Djangoで、選択した大カテゴリによって、小カテゴリの内容を絞りこむようなサンプルです。 

appは、全てのカテゴリをJavaScriptのオブジェクトで予め定義しているサンプルです。`/`でアクセスできます。

app2は、Ajaxを使う例です。`/app2/`でアクセスできます。

[ブログで解説もしています](https://narito.ninja/blog/detail/50/)

## 動かし方
```bash
git clone https://github.com/naritotakizawa/django-category-filter
cd django-category-filter
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
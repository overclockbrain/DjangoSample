# Django Note
参考にしたところ  
<https://docs.djangoproject.com/ja/4.0/intro/tutorial01/>  

## ダウンロード
~~~bash
#install mac ver...
python -m pip install Django
~~~
- Pythonが入っていれば使用可能
- Windowsはしらん...

## サイトを作る
~~~bash
#make project
django-admin startproject mysite

#change dir
cd mysite

#execute
python manage.py runserver 
~~~
- プロジェクトも調べたまんま作るくらい
- 作った**プロジェクトディレクトリに入る**の忘れない
- ローカルホストのアドレスとポート番号が表示されるからそれを入力する

## データベース(モデル)の操作
~~~bash
#データベース(Djangoで使う簡単なのはモデルという)に変更をマイグレーション(移行)する
python manage.py makemigrations polls

#SQL化する(すげええ)
#つまり、外部のDBに登録する際にコピペできるようにする
python manage.py sqlmigrate polls 0001
~~~

## adminの作成
~~~bash
#useradd
python manage.py createsuperuser

~~~
まああとはサイトを参考にコピペ作業していくわ  
> メモ
- mysite(一番上のdir)のsettings.pyで好き放題設定できる
- モデルというデータベースもどきがある
- TIME-ZONEは安心と信頼のAsia/Tokyo
- viewsはhtmlファイルを管理するファイル
- voteはチュートリアル上作らないみたい

> つまづいた事
- よくファイルパスを見てプログラムをコピらないとえぐい
- timezoneを有効化するためにfalseにしないといけない
- リンク切れてんなって思ったらviews.pyの設定ミス
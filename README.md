<h1>Django練習課題</h1>

<h2>Djangoプロジェクトの作成</h2>
以下の内容でプロジェクトを作成してください。<br/>

プロジェクト名：katachi<br/>
アプリケーション名：blog<br/>
仮想環境名：venv<br/>
必要なパッケージ：Django 3.2.10<br/>
使用するデータベース：MySQL

またこのプロジェクトを実行し、URL「<a>http://127.0.0.1:8000/</a>」でindex.htmlを表示してください。以下のような画面が表示されたら問題ありません。
<img src="./forREADME/install.jpg">

<hr>
<h2>ユーザーモデルを作ってみましょう</h2>
まずはそれぞれのユーザーを登録できるように、以下のようなパラメータを持つモデルを作ってみましょう。

<table>
    <thead>
        <tr>
            <th>パラメータ名</th>
            <td>型</td>
            <td>制約</td>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>name</td>
            <td>文字列</td>
            <td>最大20文字・入力必須</td>
        </tr>
        <tr>
            <td>birthday</td>
            <td>日付</td>
            <td>入力必須</td>
        </tr>
        <tr>
            <td>gender</td>
            <td>性別</td>
            <td>入力必須</td>
        </tr>
        <tr>
            <td>bloodtype</td>
            <td>血液型</td>
            <td>入力必須</td>
        </tr>
        <tr>
            <td>profile</td>
            <td>プロフィール</td>
            <td>入力必須</td>
        </tr>
    </tbody>
</table>
<hr>
<h2>管理画面からデータを追加してみましょう</h2>
まずは、管理画面を扱えるように管理者ユーザーをコマンドから作成してください。IDとパスワードは任意に設定頂いて構いません。</br>
管理者画面からユーザーモデルを参照して、扱えるように設定し、以下のようにデータを登録してください。
<table>
    <thead>
        <tr>
            <td>ID</td>
            <td>name</td>
            <td>birthday</td>
            <td>gender</td>
            <td>bloodtype</td>
            <td>profile</td>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>1</td>
            <td>加藤健介</td>
            <td>1990/11/10</td>
            <td>0</td>
            <td>o</td>
            <td>趣味は旅行で、今はアラスカで一人旅をしています。</td>
        </tr>
        <tr>
            <td>2</td>
            <td>田中太郎</td>
            <td>2000/10/12</td>
            <td>0</td>
            <td>b</td>
            <td>船乗りです。今はどこかの半島の沖にいます。帰りたいです。</td>
        </tr>
        <tr>
            <td>3</td>
            <td>佐藤綾子</td>
            <td>1995/4/14</td>
            <td>1</td>
            <td>a</td>
            <td>凧あげが好きです。</td>
        </tr>
    </tbody>
</table>

一覧で表示したとき、下のような画面が表示されたら問題ありません。
<img src="./forREADME/profiles.jpg">

<hr>
<h2>ユーザーの情報を一覧で表示してみましょう</h2>
URLで「<a>http://127.0.0.1:8000/users</a>」にアクセスしたら、登録しているユーザーの情報がコンソールに表示されるようにして下さい。

<hr>
<h2>ブラウザにユーザー情報を一覧で表示するようにしましょう</h2>
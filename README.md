
### Command

```sh
# app 追加
$ mkdir web
$ docker compose exec backend uv run django-admin startapp web web
$ docker compose exec backend uv run ruff check . --fix
$ docker compose exec backend uv run ruff format .
# djlint によるフォーマット
$ docker compose exec backend uv run djlint templates/*/*.html --extension=html.j2 --reformat

http://127.0.0.1:8000/

# セキュリティチェック
$ docker compose exec backend uv tool run djcheckup http://host.docker.internal:8000/web/
```

```sh
# ライブラリ追加
$ docker compose exec web uv add "Django==5.2.8"
# dev用のライブラリ追加
$ docker compose exec web uv add "djlint==1.36.4" --dev
```

### Devin

- [Devin's Machine](https://app.devin.ai/workspace) でリポジトリ追加

#### 1.Git Pull
- そのまま

#### 2.Configure Secrets
```sh
# 環境変数用のファイル作成
$ touch .envrc
$ cp .envrc.example .envrc
$ direnv allow
```

- ローカル用
```sh
$ brew install direnv
```
#### 4.Maintain Dependencies
```sh
$ docker compose up -d

# コンテナ作り直し
$ source ./remake_container.sh
```

#### 5.SetUp Lint
```sh
$ docker compose exec backend uv run ruff check .

# mypy による型ヒントチェック
$ docker compose exec backend uv run mypy .

# djlint で HTML をチェック
$ docker compose exec backend uv run djlint templates --extension html
```

#### 6.SetUp Tests
- no tests ran in 0.00s だと Devin の Verify が通らないっぽい
```sh
$ docker compose exec backend uv run pytest
```

### 7.Setup Local App

```sh
$ http://127.0.0.1:8000/がアプリケーションのURL
```

#### 8.Additional Notes
- 必ず日本語で回答してください
- Python, Django を利用する
- データベースは Postgres
- テストは pytest を利用する
を入力


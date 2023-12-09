from flask import Blueprint, jsonify, request
from werkzeug.utils import secure_filename
from Flask.models import db, Article
import os
import datetime

article = Blueprint('article', __name__, url_prefix='/article')

# 假设您的Flask应用已经配置了静态文件夹
UPLOAD_FOLDER = 'static/uploads'
BASE_URL = 'http://localhost:5000'  # 或您的实际应用基础URL
# 确保上传文件夹存在
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@article.route('/create_article', methods=['POST'])
def create_article():
    try:
        title = request.form.get('title')
        content = request.form.get('content')
        cover = request.files.get('cover')

        cover_url = ""
        if cover:
            filename = secure_filename(cover.filename)
            # 文件保存在静态目录下的UPLOAD_FOLDER中
            filepath = os.path.join(UPLOAD_FOLDER, filename)
            cover.save(filepath)
            # 生成用于访问图片的URL
            cover_url = f'{BASE_URL}/{UPLOAD_FOLDER}/{filename}'

        # 创建文章实例，存储cover的URL
        article = Article(
            title=title,
            content=content,
            cover=cover_url,
            create_time=datetime.datetime.now(),
            update_time=datetime.datetime.now()
        )
        db.session.add(article)
        db.session.commit()

        return jsonify({'id': article.id, 'message': 'Article created successfully', 'cover_url': cover_url}), 201

    except Exception as e:
        print(str(e))
        return jsonify({'message': 'Article creation failed!'}), 500


@article.route('/update_article/<int:article_id>', methods=['PUT'])
def update_article(article_id):
    try:
        article = Article.query.get(article_id)
        if not article:
            return jsonify({'message': 'Article not found'}), 404

        title = request.form.get('title')
        content = request.form.get('content')
        cover = request.files.get('cover')

        # 如果提供了新的封面图片
        if cover:
            # 如果文章已有封面，删除旧的封面文件
            if article.cover:
                old_filepath = os.path.join(UPLOAD_FOLDER, article.cover)
                if os.path.exists(old_filepath):
                    os.remove(old_filepath)

            filename = secure_filename(cover.filename)
            new_filepath = os.path.join(UPLOAD_FOLDER, filename)
            cover.save(new_filepath)
            # 生成新的封面图片URL
            cover_url = f'{BASE_URL}/{UPLOAD_FOLDER}/{filename}'
            article.cover = cover_url  # 更新数据库中的封面URL

        # 更新标题和内容
        if title:
            article.title = title
        if content:
            article.content = content

        article.update_time = datetime.now()  # 更新修改时间
        db.session.commit()

        return jsonify({'id': article.id, 'message': 'Article updated successfully', 'cover_url': article.cover}), 200

    except Exception as e:
        print(str(e))
        return jsonify({'message': 'Article update failed!'}), 500

@article.route('/delete_article/<int:article_id>', methods=['DELETE'])
def delete_article(article_id):
    article = Article.query.get(article_id)
    if not article:
        return jsonify({'message': 'Article not found'}), 404
    db.session.delete(article)
    db.session.commit()
    return jsonify({'message': 'Article deleted successfully'}), 200

@article.route('/get_article/<int:article_id>', methods=['GET'])
def get_article(article_id):
    article = Article.query.get(article_id)
    if not article:
        return jsonify({'message': 'Article not found'}), 404
    article_data = {
        'id': article.id,
        'title': article.title,
        'cover': article.cover,
        'content': article.content,
        'create_time': article.create_time.strftime("%Y-%m-%d %H:%M:%S"),
        'update_time': article.update_time.strftime("%Y-%m-%d %H:%M:%S")
    }
    return jsonify(article_data), 200

@article.route('/get_all_articles', methods=['GET'])
def get_all_articles():
    articles = Article.query.all()
    articles_data = [{
        'id': article.id,
        'title': article.title,
        'cover': article.cover,
        'content': article.content,
        'create_time': article.create_time.strftime("%Y-%m-%d %H:%M:%S"),
        'update_time': article.update_time.strftime("%Y-%m-%d %H:%M:%S")
    } for article in articles]
    return jsonify(articles_data), 200

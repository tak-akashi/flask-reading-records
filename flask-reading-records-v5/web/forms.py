from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, TextAreaField
from wtforms.fields.html5 import DateField
# from wtforms import DateField
from wtforms.validators import DataRequired

class BookForm(FlaskForm):
    title = StringField('書籍', validators=[DataRequired()])
    author = SelectField('著者', coerce=int, validators=[DataRequired()])
    genre = SelectField('ジャンル',choices=[('小説','小説'),('経営','経営'),('歴史','歴史'),('ビジネス','ビジネス'),('宗教哲学','宗教哲学'),('自然科学','自然科学'),('社会科学','社会科学'),('工学','工学'),('芸術','芸術'),('言語','言語'),('趣味','趣味'),('その他','その他')])
    date = DateField('読了日', format="%Y-%m-%d")
    recommended = SelectField('オススメ度', choices=[('5','5: とてもオススメ'),('4','4: ややオススメ'),('3','3: 普通'),('2','2: 余りオススメしない'),('1','1: 全くオススメしない')])
    comment = TextAreaField('コメント')
    submit = SubmitField('登録')

class AuthorForm(FlaskForm):
    name = StringField('著者', validators=[DataRequired()])
    extras = StringField('説明')
    submit = SubmitField('登録')

class BookUpdateForm(BookForm):
    submit = SubmitField('修正')

class AuthorUpdateForm(AuthorForm):
    submit = SubmitField('修正')

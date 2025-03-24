from flask import Flask , render_template , request , redirect , url_for
import sqlite3

app=Flask(__name__)

@app.route("/")
def index():
    conn = sqlite3.connect('database.db')
    conn.row_factory= sqlite3.Row
    posts= conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    return  render_template("index.html" , posts= posts)

@app.route("/<int:post_id>")    
def post(post_id):
    conn = sqlite3.connect('database.db')
    conn.row_factory= sqlite3.Row
    post = conn.execute('SELECT * FROM posts WHERE id=?',[post_id]).fetchone()
    conn.close()
    return render_template("post.html", post=post)
    
@app.route("/create", methods=['GET','POST'])
def create():
     if request.method=='POST':
         title= request.form['title']
         content= request.form['content']
         conn = sqlite3.connect('database.db')
         conn.row_factory= sqlite3.Row
         conn.execute('INSERT INTO posts(title,content) VALUES(?,?)',(title,content))
         conn.commit()
         conn.close()
         return redirect(url_for('index'))
     else:
         return  render_template("create.html")

@app.route("/<int:id>/edit" , methods=['GET','POST'])
def edit(id): 
    conn = sqlite3.connect('database.db')
    conn.row_factory= sqlite3.Row
    post= conn.execute('SELECT * FROM posts WHERE id=?',[id]).fetchone()
    conn.close()
    if request.method == 'POST':
        title= request.form['title']
        content= request.form['content']
        conn = sqlite3.connect('database.db')
        conn.row_factory= sqlite3.Row
        conn.execute('UPDATE posts SET title=? , content=?'
                     'WHERE id=?' , (title,content,id))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    return render_template('edit.html', post=post)

@app.route("/<int:id>/delete" , methods=["GET","POST"])
def delete(id):
    conn = sqlite3.connect('database.db')
    conn.row_factory= sqlite3.Row
    conn.execute("DELETE FROM posts WHERE id=?",[id])
    conn.commit()
    conn.close()
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True)
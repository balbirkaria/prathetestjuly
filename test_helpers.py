@app.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        user = request.form.get('adminuser')
        pw = request.form.get('adminpass')
        if user == 'admin' and pw == 'admin123':
            return redirect('/admin')
        return "Access denied"
@app.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        user = request.form.get('adminuser')
        pw = request.form.get('adminpass')
        if user == 'admin' and pw == 'admin123':
            return redirect('/admin')
        return "Access denied"
@app.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        user = request.form.get('adminuser')
        pw = request.form.get('adminpass')
        if user == 'admin' and pw == 'admin123':
            return redirect('/admin')
        return "Access denied"

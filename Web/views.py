from django.shortcuts import render, redirect
import pymysql
from utils import sqlhelper


def classes(request):
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='chen0918', db='web')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute("select id, title from class")
    class_list = cursor.fetchall()
    cursor.close()
    conn.close()

    return render(request, 'classes.html', {'class_list': class_list})


def addClass(request):
    if request.method == 'GET':
        return render(request, 'addClass.html')
    else:
        # print(request.POST)
        i = request.POST.get('id')
        v = request.POST.get('title')
        # 创建连接
        if len(v)>0:  #  填了值才能添加班级
            conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='chen0918', db='web')
            # 创建游标
            cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
            cursor.execute("insert into class(id,title) values(%s,%s)", [i, v, ])
            conn.commit()
            cursor.close()
            conn.close()
            return redirect('/classes/')
        else:
            return render(request, 'addClass.html',{'msg':'Please input class name'})


def delClass(request):
    nid = request.GET.get('nid')
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='chen0918', db='web')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute("delete from class where id = %s", [nid, ])
    conn.commit()
    cursor.close()
    conn.close()
    return redirect('/classes/')


def editClass(request):
    if request.method == "GET":
        nid = request.GET.get('nid')
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='chen0918', db='web')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute("select id,title from class where id = %s", [nid, ])
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        return render(request, 'editClass.html', {'result': result})
    else:
        nid = request.GET.get('nid')
        i = request.POST.get('id')
        v = request.POST.get('title')
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='chen0918', db='web')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute("update class set id=%s, title=%s where id = %s", [i, v, nid, ])
        conn.commit()
        cursor.close()
        conn.close()
        return redirect('/classes/')


def students(request):
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='chen0918', db='web')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute(
        "select student.id, student.stu_name, class.title from student left join class on student.class_id = class.id")
    student_list = cursor.fetchall()
    cursor.close()
    conn.close()

    return render(request, 'students.html', {'student_list': student_list})


def addStudent(request):
    if request.method == 'GET':
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='chen0918', db='web')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute("select id, title from class")
        class_list = cursor.fetchall()
        cursor.close()
        conn.close()
        return render(request, 'addStudent.html', {'class_list': class_list})
    else:
        name = request.POST.get('stu_name')
        class_id = request.POST.get('class_id')
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='chen0918', db='web')
        # 创建游标
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute("insert into student(stu_name,class_id) values(%s,%s)", [name, class_id, ])
        conn.commit()
        cursor.close()
        conn.close()
        return redirect('/students/')


def editStudent(request):
    if request.method == "GET":
        nid = request.GET.get('nid')
        result = sqlhelper.get_one('select id,stu_name,class_id from student where id=%s', [nid, ])
        class_list = sqlhelper.get_list("select id,title from class", [])
        return render(request, 'editStudent.html', {'result': result, 'class_list': class_list})
    else:
        nid = request.GET.get('nid')
        id = request.POST.get('id')
        name = request.POST.get('stu_name')
        class_id = request.POST.get('class_id')
        sqlhelper.modify("update student set id=%s, stu_name=%s, class_id=%s where id = %s",
                         [id, name, class_id, nid, ])
        return redirect('/students/')


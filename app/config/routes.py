
from system.core.router import routes

routes['default_controller'] = 'Users'
routes['GET']['/users/loginpage'] = 'Users#loginpage'
routes['POST']['/users/login'] = 'Users#login'
routes['GET']['/users/logout'] = 'Users#logout'
routes['GET']['/users/registerpage'] ='Users#register_page'
routes['POST']['/users/register'] = 'Users#register'
routes['POST']['/users/regimanager'] ='Users#regimanager'
routes['GET']['/users/dash'] = 'Users#dash'
routes['GET']['/users/editpage'] = 'Users#editpage'
routes['POST']['/users/edit'] = 'Users#edit'
routes['POST']['/users/pw'] = 'Users#pw'
routes['GET']['/admin/editpage/<id>'] = 'Admin#admin_editpage'
routes['POST']['/admin/edituser'] = 'Admin#edituser'
routes['GET']['/admin/kick/<id>'] = 'Admin#kick'
routes['GET']['/admin/dash'] = 'Admin#admin_dash'
routes['GET']['/admin/add_page'] = 'Admin#admin_add_page'
routes['POST']['/admin/pwupdate'] = 'Admin#pwupdate'
routes['GET']['/wall/<id>'] = 'Wall#show'
routes['POST']['/msg'] = 'Wall#msg'
routes['POST']['/msgdel'] = 'Wall#msgdel'
routes['POST']['/comment'] = 'Wall#comment'
routes['POST']['/cmtdel'] = 'Wall#cmtdel'
routes['POST']['/dm'] = "Wall#dm"
routes['POST']['/dmcomment'] = "Users#dmcomment"
routes['POST']['/dmcmtdel'] = "Users#dmcmtdel"
routes['/delanoun/<id>'] = 'Wall#delanoun'
routes['POST']['/addanoun'] = 'Admin#addanoun'
routes['GET']['/users/registerpage/manager'] = "Users#manager"
routes['GET']['/users/profile'] = "Users#profile"
routes['POST']['/dmdel'] = "Users#dmdel"

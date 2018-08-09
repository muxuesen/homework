import redis
import json

from django.conf import settings

from rest_framework.viewsets import ViewSetMixin
from rest_framework.views import APIView
from rest_framework.response import Response

from api import models
from api.utils.response import BaseResponse


CONN = redis.Redis(host="192.168.11.130", port=6379)
USER_ID = 1
class ShoppingCarView(ViewSetMixin,APIView):
    def list(self, request, *args, **kwargs):
        # CONN.hset("muxuesen_name", "k1", "穆学森")
        # n1 = CONN.hget("muxuesen_name", "k1").decode("utf-8")
        ret = {'code': 10000, 'data': None, 'error': None}
        try:
            shopping_car_course_list = []

            #经常用到的变量：匹配在redis存储的key,在setting中设置的"shopping_car_%s_%s"
            pattern = settings.LUFFY_SHOPPING_CAR % (USER_ID, '*',)

            #查找所有符合给定模式 pattern 的 key
            user_key_list = CONN.keys(pattern)
            """
            循环每一个key，并在redis里去取出值，赋给需要展示的相应字段，组成一个新的字典temp
            """
            for key in user_key_list:
                temp = {
                    'id': CONN.hget(key, 'id').decode('utf-8'),
                    'name': CONN.hget(key, 'name').decode('utf-8'),
                    'img': CONN.hget(key, 'img').decode('utf-8'),
                    'default_price_id': CONN.hget(key, 'default_price_id').decode('utf-8'),
                    'price_policy_dict': json.loads(CONN.hget(key, 'price_policy_dict').decode('utf-8'))
                }
                #把写有价格策略的字典temp放到列表中，再将最后的结果作为值放进key['data']里
                shopping_car_course_list.append(temp)

            ret['data'] = shopping_car_course_list
        except Exception as e:
            ret['code'] = 10005
            ret['error'] = '获取购物车数据失败'

        return Response(ret)

    def create(self, request, *args, **kwargs):

         """
         接收课程ID，价格策略ID
         django restful framework的解析器根据请求中Content-Type请求头的值，选择指定解析对请求体中的数据进行解析，
         请求头中含有Content-type: application/json 则内部使用的是JSONParser，JSONParser可以自动去请求体request.body中
          获取请求数据，然后进行 字节转字符串、json.loads反序列化；
        """
         course_id = request.data.get("courseid")
         policy_id = request.data.get("policyid")
         #判断合法性，课程是否存在？价格策略是否违法？
         course = models.Course.objects.filter(id=course_id).first()
         if not course:
             return Response({"code": 10001, "erorr": "课程不存在"})
         price_policy_query = course.price_policy.all()


         price_policy_dict ={}
         for item in price_policy_query:
             temp = {
                 "id": item.id,
                 "price": item.price,
                 "valid_period": item.valid_period,
                 "valid_period_display": item.get_valid_period_display(),
             }

            #把用户ID作为key，价格策略作为值存入字典，用来判断，价格策略是否在其中
             price_policy_dict[item.id] = temp

         if policy_id not in price_policy_dict:
             return Response({"code": 10002, "error": "价格策略别瞎改"})

         # 把商品等放入购物车
         key = "shopping_car_%s_%s" % (USER_ID, course_id)
         CONN.hset(key, "id", course_id)
         CONN.hset(key, "name", course.name)
         CONN.hset(key, 'img', course.course_img)
         CONN.hset(key, "default_price_id", policy_id)
         CONN.hset(key, "price_policy_dict", json.dumps(price_policy_dict))

         return Response({"code": 10000,"data":"购买成功"})


    def destroy(self, request, *args, **kwargs):
        response = BaseResponse()
        try:
            #取出课程ID，通过课程ID取出整条价格策略的key
            courseid = request.GET.get('courseid')
            key = settings.LUFFY_SHOPPING_CAR % (USER_ID, courseid,)

            #删除 key
            CONN.delete(key)
            response.data = '删除成功'
        except Exception as e:
            response.code = 10006
            response.error = '删除失败'
        return Response(response.dict)



    def update(self,  request, *args, **kwargs):
        response = BaseResponse()
        try:     #取出课程ID、要修改的价格策略ID
            course_id = request.data.get('courseid')
            policy_id = str(request.data.get('policyid')) if request.data.get('policyid') else None


            key = settings.LUFFY_SHOPPING_CAR % (USER_ID, course_id,)
            #在redisz中校验合法性
            if not CONN.exists(key):
                response.code = 10007
                response.error = '课程不存在'
                return Response(response.dict)

            price_policy_dict = json.loads(CONN.hget(key, 'price_policy_dict').decode('utf-8'))
            if policy_id not in price_policy_dict:
                response.code = 10008
                response.error = '价格策略不存在'
                return Response(response.dict)

            CONN.hset(key, 'default_price_id', policy_id)
            CONN.expire(key, 20 * 60)
            response.data = '修改成功'
        except Exception as e:
            response.code = 10009
            response.error = '修改失败'

        return Response(response.dict)













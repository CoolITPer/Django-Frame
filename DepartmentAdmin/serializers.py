from rest_framework import serializers

from DepartmentAdmin.models import BookInfo


class BookInfoSerializer(serializers.Serializer):#ModelSerializer
    '''图书数据序列化器
    model 指明该序列化器处理的数据字段从模型类BookInfo参考生成
    fields 指明该序列化器包含模型类中的哪些字段'''
    # class Meta:
    #     model = BookInfo
    #     fields = '__all__'

    # def about_django(value):   #配合validators=[about_django]进行验证
    #     if 'django' not in value.lower():
    #         raise serializers.ValidationError("图书不是关于Django的")

    '''只有阅读量大于评论量才能验证通过'''
    # def validate(self, attrs):
    #     bread = attrs['bread']
    #     bcomment = attrs['bcomment']
    #     if bread < bcomment:
    #         raise serializers.ValidationError('阅读量小于评论量')
    #     return attrs

    # def validate_btitle(self, value):  #想要检验某个字段就在改序列化器中定义validate_字段
    #
    # if 'django' not in value.lower():
    #     raise serializers.ValidationError("图书不是关于Django的")
    # return value

    id = serializers.IntegerField(label='ID', read_only=True)
    btitle = serializers.CharField(label='名称', max_length=20)
    bpub_date = serializers.DateField(label='发布日期', required=False)
    bread = serializers.IntegerField(label='阅读量', required=False)
    bcomment = serializers.IntegerField(label='评论量', required=False)
    image = serializers.ImageField(label='图片', required=False)


    def create(self, validated_data):
        """新建"""
        return BookInfo.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """更新，instance为要更新的对象实例"""
        instance.btitle = validated_data.get('btitle', instance.btitle)
        # instance.bpub_date = validated_data.get('bpub_date', instance.bpub_date,required=False)
        # instance.bread = validated_data.get('bread', instance.bread,required=False)
        # instance.bcomment = validated_data.get('bcomment', instance.bcomment,required=False)
        instance.save()
        return instance
    

class HeroInfoSerializer(serializers.Serializer):
    """英雄数据序列化器"""
    GENDER_CHOICES = (
        (0, 'male'),
        (1, 'female')
    )
    id = serializers.IntegerField(label='ID', read_only=True)
    hname = serializers.CharField(label='名字', max_length=20)
    hgender = serializers.ChoiceField(choices=GENDER_CHOICES, label='性别', required=False)
    hcomment = serializers.CharField(label='描述信息', max_length=200, required=False, allow_null=True)
    hbook = serializers.PrimaryKeyRelatedField(label='图书', read_only=True)   #关联对象嵌套序列化通过英雄查询书
    # heroinfo_set = serializers.PrimaryKeyRelatedField(read_only=True, many=True)  # 新增

class BookInfoReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookInfo
        fields = ['bread']
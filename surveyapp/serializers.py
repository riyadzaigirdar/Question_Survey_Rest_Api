from rest_framework import serializers
from . import models



class AdminAnswerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Answer
        fields = ['candidiate','ans']
             

class QuestionAdminSerializer(serializers.ModelSerializer):

    response = AdminAnswerSerializer(many=True, read_only = True)
    
    class Meta:
        model = models.Question
        fields = ['id', 'title','response']


class AnswerUserSerializer(serializers.ModelSerializer):
    '''
    ques = serializers.StringRelatedField()
    candidiate = serializers.StringRelatedField()
    '''

    class Meta:
        model = models.Answer
        fields = ['id', 'ques', 'candidiate', 'ans']
        read_only_fields = ['id']
        
        
    def create(self,validated_data):
        ans_obj = models.Answer.objects.create(**validated_data)
        ques = validated_data['ques']
        ques_obj = models.Question.objects.get(title = ques)
        ques_obj.response.add(ans_obj)

        return ans_obj


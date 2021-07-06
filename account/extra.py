
"""
class Account (AbstractUser):
    facebook_id = BigIntegerField(primary_key=True)
    name = models.CharField(max_length=300)
    image = models.FileField(upload_to="media/", null=True, verbose_name="")


class Profile(User):
    user = models.OneToOneField(
        Account, on_delete=models.CASCADE, parent_link=True)
    birth_date = models.CharField(max_length=20)
    age = models.IntegerField(null=False)
    gender = models.CharField(max_length=10)
    personal_description = models.CharField(max_length=1000)
    city = models.CharField(max_length=200)
    course = models.CharField(max_length=1000)
    admission = models.CharField(max_length=300)
    flat_finder = models.CharField(max_length=100)
    sharing_preferences = models.CharField(max_length=40)
    food_preferences = models.CharField(max_length=100)
    cooking_skills = models.CharField(max_length=300)
    personality = models.CharField(max_length=20000)
"""

"""
class ProfileViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('id', 'age', 'facebook_id', 'email', 'name', 'image', 'birth_date', 'gender', 'personal_description', 'city',
                  'course', 'admission', 'flat_finder', 'sharing_preferences', 'food_preferences', 'cooking_skills', 'personality')


class ProfileCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('id', 'age', 'facebook_id', 'email', 'name', 'image', 'birth_date', 'gender', 'personal_description', 'city',
                  'course', 'admission', 'flat_finder', 'sharing_preferences', 'food_preferences', 'cooking_skills', 'personality')

    def validate(self, validated_data):
        if Account.objects.filter(email=validated_data['email']).exists():
            raise serializers.ValidationError(
                {"success": False, "response": "email already exists"})
        if Account.objects.filter(facebook_id=validated_data['facebook_id']).exists():
            raise serializers.ValidationError(
                {"success": False, "response": "facebook id already exists"})
        if validated_data["gender"] == "Male":
            gender1 = 'M'
        elif validated_data["gender"] == "Female":
            gender1 = "F"
        elif validated_data["gender"] == "Non-Binary":
            gender1 = "NB"
        elif validated_data['gender'] == "":
            raise serializers.ValidationError(
                {"success": False, "reponse": "Gender is a compulsory field"})
        if validated_data["city"] == "":
            raise serializers.ValidationError(
                {"success": False, "reponse": "City is a compulsory field"})
        if validated_data["admission"] == "":
            raise serializers.ValidationError({
                "success": False, "response": "Admission is a compulsory field"
            })
        if validated_data["course"] == "":
            raise serializers.ValidationError(
                {"success": False, "response": "Course is a compulsory field"})
        if validated_data["flat_finder"] == "":
            raise serializers.ValidationError(
                {"success": False, "response": "Flat finding details are essential"})
        if validated_data["sharing_preferences"] == "":
            raise serializers.ValidationError(
                {"success": False, "response": "Sharing Preferences are essential"})
        if validated_data["food_preferences"] == "":
            raise serializers.ValidationError(
                {"success": False, "response": "Food prefernce is an essential field"})
        if validated_data["cooking_skills"] == "":
            raise serializers.ValidationError(
                {"success": False, "response": "cooking skills are essential"})

        profile = Account.objects.create(
            age=validated_data["age"],
            facebook_id=validated_data["facebook_id"],
            email=validated_data["email"],
            name=validated_data["name"],
            image=validated_data["image"],
            birth_date=validated_data["birth_date"],
            gender=gender1,
            personal_description=validated_data["personal_description"],
            city=validated_data["city"],
            course=validated_data["course"],
            admission=validated_data["admission"],
            flat_finder=validated_data["flat_finder"],
            sharing_preferences=validated_data["sharing_preferences"],
            food_preferences=validated_data["food_preferences"],
            cooking_skills=validated_data["cooking_skills"],
            personality=validated_data["personality"]
        )
        return profile
"""

"""
    birth_date=birth_date,
    gender=gender,
    personal_description=personal_description,
    city=city,
    course=course,
    admission=admission,
    flat_finder=flat_finder,
    sharing_preferences=sharing_preferences,
    food_preferences=food_preferences,
    cooking_skills=cooking_skills,
    personality=personality,
    age=age
"""

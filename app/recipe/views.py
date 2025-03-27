"""
Views for the recipe api
"""
from rest_framework import viewsets # type: ignore
from rest_framework.authentication import TokenAuthentication # type: ignore 
from rest_framework.permissions import IsAuthenticated # type: ignore

from core.models import Recipe, Tag, Ingredient
from recipe import serializers

from rest_framework import viewsets, mixins # type: ignore

class RecipeViewSet(viewsets.ModelViewSet):
    """Manage recipes in the database"""
    serializer_class = serializers.RecipeDetailSerializer
    queryset = Recipe.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


    def get_queryset(self):
        """Retrieve the recipes for the authenticated user"""
        return self.queryset.filter(user=self.request.user).order_by('-id')

    def get_serializer_class(self):
        """Return appropriate serializer class"""
        if self.action == 'list':
            return serializers.RecipeSerializer
        return self.serializer_class
    
    def perform_create(self, serializer):
        """Create a new recipe"""
        serializer.save(user=self.request.user)

class BaseRecipeAttrViewSet(viewsets.GenericViewSet, 
                 mixins.ListModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.DestroyModelMixin):
    """Base view set for recipe attributes"""
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Return tags for the current authenticated user"""
        return self.queryset.filter(user=self.request.user).order_by('-name')


class TagViewSet(BaseRecipeAttrViewSet):
    """Manage tags in the database"""
    serializer_class = serializers.TagSerializer
    queryset = Tag.objects.all()
    

class IngredientViewSet(BaseRecipeAttrViewSet):
    """Manage ingredients in DB"""
    serializer_class = serializers.IngredientSerializer
    queryset = Ingredient.objects.all()

    
    

from django.contrib import admin

from rooms.models import Room, Amenity


@admin.action(description="Set all prices to zero")
def reset_prices(model_admin, request, queryset):
    for room in queryset.all():
        room.price = 0
        room.save()


# Register your models here.
# Register your models here.
@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):

    actions = (reset_prices,)
    list_display = (
        'name',
        'price',
        'kind',
        'total_amenities',
        'rating',
        'owner',
        'created_at',
        'updated_at'
    )

    list_filter = (
        'country',
        'city',
        'price',
        'rooms',
        'toilets',
        'pet_friendly',
        'kind',
        'amenities',
        'created_at',
        'updated_at'
    )

    search_fields = (
        'name',
        'price',
        "owner__username"
    )


@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
        'created_at',
        'updated_at'
    )
    readonly_fields = (
        'created_at',
        'updated_at'
    )

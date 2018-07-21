from django.views.generic import ListView

from app.models import House, Housemate


class HouseListView(ListView):
    model = House
    paginate_by = 10

    def get_queryset(self):
        queryset = super(HouseListView, self).get_queryset()
        if self.kwargs.get('sort'):
            sort_by = self.kwargs.get('sort')
            return queryset.order_by(sort_by)
        return queryset


class HousematesListView(ListView):
    model = Housemate
    paginate_by = 10


class HouseHousematesListView(ListView):
    model = Housemate
    template_name = 'app/housemate_list.html'
    paginate_by = 10

    def get_queryset(self):
        queryset = super(HouseHousematesListView, self).get_queryset()
        return queryset.filter(house_id=self.kwargs['pk'])

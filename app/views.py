from django.views.generic import ListView

from app.models import House, Housemates


class HouseListView(ListView):
    model = House
    paginate_by = 10

    def get_queryset(self):
        queryset = super(HouseListView, self).get_queryset()
        if self.request.GET.get('sort'):
            sort_by = self.request.GET.get('sort')
            return queryset.order_by(sort_by)
        return queryset


class HousematesListView(ListView):
    model = Housemates
    paginate_by = 10


class HouseHousematesListView(ListView):
    model = Housemates
    template_name = 'app/housemates_list.html'
    paginate_by = 10

    def get_queryset(self):
        queryset = super(HouseHousematesListView, self).get_queryset()
        return queryset.filter(house_id=self.kwargs['pk'])

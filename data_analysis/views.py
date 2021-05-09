import self as self
from django.shortcuts import render
import pymysql
import pandas as pd
import re
from data_analysis import Analyzer
import json
from django.views.generic import ListView
from .models import Company, DailyPrice
from django.db.models import Q
from django.core.serializers.json import DjangoJSONEncoder


class CompanyList(ListView):
    model = Company
    template_name = 'data_analysis/company_list.html/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data = list(Company.objects.values())

        context["qs_json"] = json.dumps(list(Company.objects.values()), cls=DjangoJSONEncoder)
        return context


class CompanySearch(CompanyList):
    paginate_by = None

    def get_queryset(self):
        q = self.kwargs['q']
        company_list = Company.objects.filter(
            Q(company__contains=q) | Q(code__contains=q)
        ).distinct()
        return company_list

    def get_context_data(self, **kwargs):
        context = super(CompanySearch, self).get_context_data()
        q = self.kwargs['q']
        context['search_info'] = f'검색 결과 : {q} ({self.get_queryset().count()})'

        return context


class DailyPriceList(ListView):
    model = DailyPrice
    paginate_by = 20
    ordering = '-pk'
    template_name = 'data_analysis/daily_price.html/'

    def get_queryset(self):
        daily_price_all = DailyPrice.objects.extra(tables=['company_info'], where=['company_info.code=daily_price.code'])

        return daily_price_all

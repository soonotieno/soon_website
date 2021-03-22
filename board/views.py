from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from .models import Board, BoardComment
from .forms import CommentForm
from django.db.models import Q


class BoardList(ListView):
    model = Board
    ordering = '-pk'
    paginate_by = 7


class BoardDetail(DetailView):
    model = Board

    def get_context_data(self, **kwargs):
        context = super(BoardDetail, self).get_context_data()
        context['comment_form'] = CommentForm
        return context


class BoardCreate(LoginRequiredMixin, CreateView):
    model = Board
    fields = ['title', 'content', 'board_image', ]

    def form_valid(self, form):
        current_user = self.request.user
        if current_user.is_authenticated:
            form.instance.author = current_user
            return super(type(self), self).form_valid(form)
        else:
            return redirect('/board/free_board/')


class BoardUpdate(LoginRequiredMixin, UpdateView):
    model = Board
    fields = ['title', 'content', 'board_image', ]
    template_name = 'board/board_update.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user == self.get_object().author:
            return super(BoardUpdate, self).dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied


def new_comment(request, pk):
    if request.user.is_authenticated:
        board = get_object_or_404(Board, pk=pk)

        if request.method == 'POST':
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.board = board
                comment.author = request.user
                comment.save()
                return redirect(comment.get_absolute_url())
        else:
            return redirect(board.get_absolute_url())
    else:
        raise PermissionDenied


class CommentUpdate(LoginRequiredMixin, UpdateView):
    model = BoardComment
    form_class = CommentForm

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user == self.get_object().author:
            return super(CommentUpdate, self).dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied


def delete_comment(request, pk):
    comment = get_object_or_404(BoardComment, pk=pk)
    board = comment.board
    if request.user.is_authenticated and request.user == comment.author:
        comment.delete()
        return redirect(board.get_absolute_url())
    else:
        raise PermissionDenied


class BoardSearch(BoardList):
    paginate_by = None

    def get_queryset(self):
        q = self.kwargs['q']
        object_list = Board.objects.filter(Q(title__contains=q) | Q(content__contains=q))
        return object_list

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(BoardSearch, self).get_context_data()
        context['search_info'] = "'{}' 검색 결과".format(self.kwargs['q'])
        return context


def delete_board(request, pk):
    board = Board.objects.get(pk=pk)
    if request.user == board.author:
        board.delete()
        return redirect('/board/free_board/')
    else:
        raise PermissionError('댓글을 삭제할 권한이 없습니다.')

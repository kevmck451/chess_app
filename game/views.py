from django.shortcuts import render, redirect
from django.http import JsonResponse

from .helpers import is_ajax
from .movePieces import movePieces
from .helpers import is_valid_move, is_checkmate, get_legal_moves, initialize_board, update_board, \
    board_to_json, resign_game, offer_draw, suggest_move, log_move_history, get_move_history, validate_input, handle_error
from .forms import ColorSelectionForm
from .controller import controller

from .engine import MiniMax

import math,csv,time

def chooseMode(request):
    return render(request, 'choosePage.html')

def playLocal(request):
    return render(request, 'chessPage.html',{'aiCol':None})

def playAI(request):
    return render(request, 'chessPage.html',{'aiCol':request.session['aiColor']})

def board(request):
    if 'turn' in request.session:
        turn = request.session['turn']
    else:
        # True light, False dark
        request.session['turn'] = True
        turn = request.session['turn']

    if 'board' in request.session:
        board = request.session['board']
    else:
        request.session['board'] = [
            ["r", "n", "b", "q", "k", "b", "n", "r"],
            ["p", "p", "p", "p", "p", "p", "p", "p"],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["P", "P", "P", "P", "P", "P", "P", "P"],
            ["R", "N", "B", "Q", "K", "B", "N", "R"]
        ]
        board = request.session['board']

    if 'movedStatus' in request.session:
        movedStatus = request.session['movedStatus']
    else:
        # First element for dark, second for light
        # 00r - 04k - 07r || 70R - 74K - 77R 
        request.session['movedStatus'] = [(False,False,False),(False,False,False)]
        movedStatus = request.session['movedStatus']

    if 'enPassant' in request.session:
        enPassant = request.session['enPassant']
    else:
        request.session['enPassant'] = False,"",""
        enPassant = request.session['enPassant']

    if 'captureStatus' in request.session:
        captureStatus = request.session['captureStatus']
    else:
        # 0 for dark | 1 for light
        request.session['captureStatus'] = [(),()]
        captureStatus = request.session['captureStatus']

    if 'aiColor' in request.session:
        aiColor = request.session['aiColor']
    else:
        request.session['aiColor'] = None
        aiColor = request.session['aiColor']



    if is_ajax(request):
        square = request.POST.get('sqId')

        newSquare = request.POST.get('newSqId')
        oldSquare = request.POST.get('oldSqId')

        aiCol = request.POST.get('aiCol')
        if aiCol == 'False':
            aiCol = False
        if aiCol == 'True':
            aiCol = True
        
        jsResponseInfo = {
            'board': board,
            'turn': turn
        }
        

        if square:
            moves, checkMate,draw = controller(square, board, turn,movedStatus,enPassant)
            return JsonResponse({'moves': moves,'checkMate':checkMate, 'draw':draw, 'captureStatus':captureStatus})
        
        
        if newSquare:
            request.session['board'] = movePieces(oldSquare, newSquare, board,movedStatus,enPassant,captureStatus)
            request.session['turn'] = not request.session['turn']
            turn = request.session['turn']
            newRs= {
                'board':board,
                'turn':turn
            }
            
            return JsonResponse(newRs)

        
    
        if aiCol == turn:
            startTime = time.time()
            aiMoves = MiniMax(board, 3,-math.inf,math.inf, turn)
            endTime = time.time()
            timeDelta = endTime - startTime
            request.session['turn'] = not request.session['turn']
            turn = request.session['turn']
            request.session['board'] = movePieces(aiMoves[1][1], aiMoves[1][2], board, movedStatus, enPassant, captureStatus)
            
            with open('data.csv','a') as file:
                writer = csv.writer(file)
                writer.writerow([aiMoves[2],timeDelta])
            
            newRs= {
                'board':board,
                'turn':turn
            }
            return JsonResponse(newRs)

        
        return JsonResponse(jsResponseInfo)


    if request.method =='POST':
        playColor = request.POST.get('mySelect')
        if playColor == 'white':
            request.session['aiColor'] = False
        elif playColor == 'black':
            request.session['aiColor'] = True
            
        return redirect('playAI')

def some_view(request):
    # Example usage of helper functions
    board = initialize_board()
    move = "e2 e4"

    if is_valid_move(board, move):
        update_board(board, move)
    else:
        handle_error("Invalid move!")

    legal_moves = get_legal_moves(board, "e2")
    is_mate = is_checkmate(board, "white")
    return render(request, 'template.html', context)

def resetBoard(request):
    request.session['board'] = [
            ["r", "n", "b", "q", "k", "b", "n", "r"],
            ["p", "p", "p", "p", "p", "p", "p", "p"],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["P", "P", "P", "P", "P", "P", "P", "P"],
            ["R", "N", "B", "Q", "K", "B", "N", "R"]
        ]
    request.session['turn'] = True
    request.session['movedStatus'] = [(False,False,False),(False,False,False)]

    request.session['enPassant'] = False,"",""
    request.session['captureStatus'] = [(),()]
    request.session['aiColor'] = None

    with open('data.csv','a') as file:
        writer = csv.writer(file)
        writer.writerow(['iterations','time'])
    return redirect('chooseMode')

def selectColor(request):
    if request.method == 'POST':
        selected_color = request.POST.get('color')
        if selected_color in ['white', 'black']:
            request.session['player_color'] = selected_color
            return redirect('playLocal')  
    return render(request, 'choosePage.html')

def instructions(request):
    return render(request, 'instructions.html')

def quit_confirmation(request):
    return render(request, 'quit_confirmation.html')

def quit_game(request):
    request.session.clear()  
    return redirect('home') 

def select_color(request):
    if request.method == 'POST':
        form = ColorSelectionForm(request.POST)
        if form.is_valid():
            selected_color = form.cleaned_data['player_color']
            # Do something with the selected color
    else:
        form = ColorSelectionForm()

    return render(request, 'select_color.html', {'form': form})

def home(request):
    return render(request, 'home.html')

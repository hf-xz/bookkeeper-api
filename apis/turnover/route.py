from fastapi import APIRouter, Body

from common.response import *

from .model import *
from .service import *

router = APIRouter()


@router.post('', response_description='Turnover data added into the database')
def add_turnover_data(turnover: TurnoverSchema = Body(...)):
    '''
    添加营业额数据
    '''
    turnover = turnover.model_dump()
    # 检查是否已有相同日期的数据
    turnover_exist = retrieve_turnover_by_date(turnover['date'])
    if turnover_exist:
        return ErrorResponse(
            'Duplicate Error',
            400,
            f'Turnover with date {turnover['date']} already exists',
        )
    # 添加数据
    new_turnover = add_turnover(turnover)
    return Response(new_turnover, 'Turnover added successfully.')


@router.get('', response_description='Turnovers retrieved')
def get_turnovers():
    '''
    获取所有营业额数据
    '''
    turnovers = retrieve_turnovers()
    if turnovers:
        return Response(turnovers, 'Turnovers data retrieved successfully')
    return Response(turnovers, 'Empty list returned')


@router.get('/{id}', response_description='Turnover data retrieved')
def get_turnover_data(id):
    '''
    获取指定ID的营业额数据
    '''
    turnover = retrieve_turnover(id)
    if turnover:
        return Response(turnover, 'Turnover data retrieved successfully')
    return ErrorResponse('An error occurred.', 404, 'Turnover doesn\'t exist.')


@router.get('/date/{date}', response_description='Turnover data retrieved')
def get_turnover_data_by_date(date):
    '''
    获取指定日期的营业额数据
    '''
    turnover = retrieve_turnover_by_date(date)
    if turnover:
        return Response(turnover, 'Turnover data retrieved successfully')
    return ErrorResponse('An error occurred.', 404, 'Turnover doesn\'t exist.')


@router.put('/{id}')
def update_turnover_data(id: str, req: UpdateTurnoverModel = Body(...)):
    '''
    更新指定ID的营业额数据
    '''
    req = {k: v for k, v in req.model_dump().items() if v is not None}
    updated_turnover = update_turnover(id, req)
    if updated_turnover:
        return Response(
            f'Turnover with ID: {id} update is successful',
            'Turnover updated successfully',
        )
    return ErrorResponse(
        'An error occurred',
        404,
        'There was an error updating the turnover data.',
    )


@router.put('/date/{date}')
def update_turnover_data_by_date(date: str, req: UpdateTurnoverModel = Body(...)):
    '''
    更新指定日期的营业额数据
    '''
    req = {k: v for k, v in req.model_dump().items() if v is not None}
    updated_turnover = update_turnover_by_date(date, req)
    if updated_turnover:
        return Response(
            f'Turnover with date: {date} update is successful',
            'Turnover updated successfully',
        )
    return ErrorResponse(
        'An error occurred',
        404,
        'There was an error updating the turnover data.',
    )


@router.delete('/{id}', response_description='Turnover data deleted from the database')
def delete_turnover_data(id: str):
    '''
    删除指定ID的营业额数据
    '''
    deleted_turnover = delete_turnover(id)
    if deleted_turnover:
        return Response(
            f'Turnover with ID: {id} removed', 'Turnover deleted successfully'
        )
    return ErrorResponse(
        'An error occurred', 404, f'Turnover with id {id} doesn\'t exist'
    )

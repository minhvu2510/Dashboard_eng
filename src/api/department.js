import request from '@/utils/request'

export function addExtension(data) {
  return request({
    url: '/extension',
    method: 'post',
    data
  })
}
export function addNote(data) {
  return request({
    url: '/note',
    method: 'post',
    data
  })
}
export function getExtention(params) {
  return request({
    url: '/extension',
    method: 'get',
    params
  })
}
export function userInfor(params) {
  return request({
    url: '/user',
    method: 'get',
    params
  })
}
export function getNote(params) {
  return request({
    url: '/note',
    method: 'get',
    params
  })
}
export function updateDepartment(data) {
  return request({
    url: '/department',
    method: 'put',
    data
  })
}

export function deleteDepartment(params) {
  return request({
    url: 'department',
    method: 'delete',
    data: params
  })
}


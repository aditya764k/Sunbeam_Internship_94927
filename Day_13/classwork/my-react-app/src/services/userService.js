import axios from 'axios'
import config from './config'

export async function loginUser(email,password){
    const URL = config.BASE_URL + "/auth/login"
    const body = {email,password}
    const response = await axios.post(URL,body)
    return response.data
}

export async function registerUser(courseId,email,name,mobileNo){
    const URL = config.BASE_URL + "/student/register-to-course"
    const body = { courseId,email,name,mobileNo}
    const response = await axios.post(URL,body)
    return response.data
}


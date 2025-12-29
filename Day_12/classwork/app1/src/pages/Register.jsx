import React, { useState } from 'react'
import { Link, useNavigate } from 'react-router'
import { registerUser } from '../services/userService'
import { toast } from 'react-toastify'

export default function Register(){
    const [courseId , setCourseId] = useState('')
    const [email,setEmail] = useState('')
    const [name,setName] = useState('')
    const [mobileNo, setMobileNo] = useState('')
    const navigate = useNavigate()

    const signup = async () => {
        if (courseId == '')
            toast.warn('name must be entered')
        else if (email == '')
            toast.warn('email must be entered')
        else if (name == '')
            toast.warn('password must be entered')
        else if (mobileNo == '')
            toast.warn('mobile must be entered')
        else{
            const result = await registerUser(courseId,email,name,mobileNo)
            if(result.status == 'success') {
                navigate('/')
                toast.success('user registered successsfully')
            } else
                toast.error(result.error)
        }

    }
    return(
        <div className='container w-50'>
            <div className=" mt-3 mb-3">
                <label htmlFor="inputcourseId" className="form-label">courseId</label>
                <input type="number" className="form-control" id="inputName" placeholder="Enter CourseId" onChange={e => setCourseId(e.target.value)} required />
            </div>

            <div className="mb-3">
                <label htmlFor="inputEmail" className="form-label">Email</label>
                <input type="email" className="form-control" id="inputEmail" placeholder="Enter email" onChange={e => setEmail(e.target.value)} required />
            </div>

            <div className="mb-3">
                <label htmlFor="inputName" className="form-label">Name</label>
                <input type="text" className="form-control" id="inputName" placeholder="Enter Name" onChange={e => setName(e.target.value)} required />
            </div>

            <div className="mb-3">
                <label htmlFor="inputMobileNo" className="form-label">MobileNo</label>
                <input type="tel" className="form-control" id="inputMobileNo" placeholder="Enter Mobile number" onChange={e => setMobileNo(e.target.value)} required />
            </div>


            <div className="mb-3">
                <button className="btn btn-success" onClick={signup}>Signup</button>
            </div>

            <div>
                Already have an account? then to login <Link to='/' >Click Here</Link>
            </div>
        </div>
    )
   
}
import React,{ useContext, useState } from "react"
import { Link, useNavigate } from "react-router"
import { loginUser } from '../services/userService'
import { toast } from "react-toastify"
import { LoginContext } from "../App"

export default function Login(){
    const [email,setEmail] = useState('')
    const [password, setPassword] = useState('')
    const navigate = useNavigate()
    const {loginStatus,setLoginStatus} = useContext(LoginContext)

    const signin = async (event) => {
        if (email == '')
            toast.warn('email must be entered')
        else if (password == '')
            toast.warn('password must be entered')
        else {
            const result = await loginUser(email,password)
            console.log(result)
            if (result.status == 'success'){
                sessionStorage.setItem('token', result.data.token)
                setLoginStatus(true)
                navigate('/home')
                toast.success("login successsful")
            }
            else
                toast.error(result.error)
        }
    }

    return (
        <div className='container w-50'>
            <div className=" mt-3 mb-3">
                <label htmlFor="inputEmail" className="form-label">Email</label>
                <input type="email" className="form-control" id="inputEmail" placeholder="Enter email" onChange={event => setEmail(event.target.value)} />
            </div>

            <div className="mb-3">
                <label htmlFor="inputPassword" className="form-label">Password</label>
                <input type="password" className="form-control" id="inputPassword" placeholder="Enter password" onChange={e => setPassword(e.target.value)} />
            </div>

            <div className="mb-3">
                <button className="btn btn-success" onClick={signin}>Signin</button>
            </div>

            <div>
                Don't have an account? then to register <Link to='/register' >Click Here</Link>
            </div>
        </div>

    )
    
}

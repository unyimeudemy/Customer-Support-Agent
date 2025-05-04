import { useNavigate } from "react-router-dom"



const DashBoard = () => {
    const navigate = useNavigate()


  return (
    <div className="h-full w-full  rounded-tl-[50px] bg-[#e6e6e6]">
        <div className=" text-yellow font-bold text-[60px]">Home</div>
        <button 
            className=" h-[50px] w-[200px] bg-red text-black border border-blue-200"
            onClick={() => navigate("/setting")}
        >Click here</button>
      
    </div>
  )
}

export default DashBoard

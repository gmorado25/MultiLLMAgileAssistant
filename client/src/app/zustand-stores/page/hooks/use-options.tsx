"use client";
import axios from "axios";
import { useEffect, useState } from "react";
import { getJSONHeader } from "@/app/utils/cookies";

const useOptions = (origin: string) => {
        
    const [options, setOptions] = useState<string[]>([]);
    
    useEffect(() => {
        
        const fetchData = () => {
            return axios.get(origin, getJSONHeader());
        }
    
        const onUpdateOptions = (isCurrent: boolean) => {
            fetchData().then((response: any) => {
                if (isCurrent)
                    setOptions(response.data);
            }).catch(e => {
                console.log(e);
            });
        }

        let isCurrent = true;               // set current flag when component mounts and renders
        onUpdateOptions(isCurrent);         // perform an async data fetch
        return () => {isCurrent = false};   // reset flag on unmount to false to prevent race conditions if the component re-renders before the data fetch completes.
    }, []);

    return options;
};

export default useOptions;
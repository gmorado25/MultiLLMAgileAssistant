"use client";
import axios from "axios";
import { useLLMStore } from "@/app/zustand-stores/page/store/LLM-store";
import { FC, useEffect, useState } from "react";
import { getJSONHeader } from "@/app/utils/cookies";

/**
 * Component designed to display the format string selected
 * by the user.
 * 
 * @param 
 * 
 * @returns 
 */
const FormatDisplay: FC = () => {

    const [content, setContent] = useState("");

    let format = useLLMStore.use.format();

    useEffect(() => {

        let url = `/formats/search.json/?format=${format}`
        
        const fetchData = () => {
            return axios.get(url, getJSONHeader());
        }
    
        const onUpdateOptions = () => {
            fetchData().then((response: any) => {
                if (isCurrentRequest)
                    setContent(response.data['description']);
            }).catch(e => {
                console.log(e);
            });
        }

        let isCurrentRequest = true;
        onUpdateOptions();
        return () => {isCurrentRequest = false};

    }, [format]);

    return(
        <>{content}</>
    );
};

export default FormatDisplay;
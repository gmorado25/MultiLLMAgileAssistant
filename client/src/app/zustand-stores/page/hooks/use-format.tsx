import axios from "axios";
import { setSelectedFormatDescription, useLLMStore } from "@/app/zustand-stores/page/store/LLM-store";
import { useEffect, useState } from "react";
import { getJSONHeader } from "@/app/utils/cookies";

const useFormat = () => {
    let format = useLLMStore.use.selectedFormat();
    const [content, setContent] = useState("");

    useEffect(() => {

        let url = `/formats/search.json/?format=${format}`
        
        const fetchData = () => {
            return axios.get(url, getJSONHeader());
        }
    
        const onUpdateOptions = () => {
            fetchData().then((response: any) => {
                if (isCurrentRequest) {
                    setContent(response.data.description);
                    setSelectedFormatDescription(response.data.description);
                }
            }).catch(e => {
                console.log(e);
            });
        }

        let isCurrentRequest = true;
        if (format === undefined) {
            setContent("")
            setSelectedFormatDescription("");
        } else
            onUpdateOptions();
        return () => {isCurrentRequest = false};

    }, [format]);
    
    return content;
}

export default useFormat;
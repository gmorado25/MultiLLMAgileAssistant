"use client";
import React, { FC, useEffect, useState } from "react";
import Option from "@mui/joy/Option";
import { Select } from "@mui/material";
import axios from "axios";
import { getJSONHeader } from "@/app/utils/cookies";

interface SelectorFields {
    origin: string, 
    default: string
};

/**
 * 
 * @param origin The
 * @returns 
 */
const AsyncSelector: FC<SelectorFields> = (field: SelectorFields) => {

    const fetchData = () => {
        return axios.get(field.origin, getJSONHeader());
    }

    const onUpdateOptions = (isCurrent: boolean) => {
        fetchData().then((response: any) => {
            if (isCurrent)
                setOptions(response.data);
        }).catch(e => {
            console.log(e);
        });
    }

    const optionOf = (url: string) => {
        return options.map(option => {
            return (
                <><Option value={option} key={option}>{option}</Option></>
            );
        });
    };
    
    const [options, setOptions] = useState<string[]>([]);
    
    useEffect(() => {
        let isCurrent = true;               // set current flag when component mounts and renders
        onUpdateOptions(isCurrent);         // perform an async data fetch
        return () => {isCurrent = false};   // reset flag on unmount to false to prevent race conditions if the component re-renders before the data fetch completes.
    }, [onUpdateOptions]);

    return(
        <Select className=" ml-4 mr-4" placeholder={field.default}>
            {optionOf(field.origin)};
        </Select>
    );
};

export default AsyncSelector;
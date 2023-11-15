"use client";
import { FC } from "react";
import { Divider } from "@mui/material";

interface DisplayType {
    heading: string,
    hook: any
}
/**
 * Component designed to display the option description selected
 * by the user.
 * 
 * @param title The heading to display above the display content
 * @param hook The hook to retrieve content on update
 * 
 * @returns 
 */
const OptionDisplay: FC<DisplayType> = ({heading, hook}: DisplayType) => {

    let content = hook();

    const displayContent = (content: string) => {
        if (content === "")
            return ""
        else
            return <><h3>{heading}:</h3>{content}<br /></>
    }

    return(
        <>
        <div>
            <Divider></Divider>
            {displayContent(content)}
        </div>
        </>
    );
};

export default OptionDisplay;
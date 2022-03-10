from RemiRobot import dispatcher
from RemiRobot.modules.disable import DisableAbleCommandHandler
from telegram import Update
from telegram.ext import CallbackContext, run_async


@run_async
def shout(update: Update, context: CallbackContext):
    args = context.args
    text = " ".join(args)
    result = [' '.join(list(text))]
    result.extend(
        f'{symbol} ' + '  ' * pos + symbol
        for pos, symbol in enumerate(text[1:])
    )

    result = list("\n".join(result))
    result[0] = text[0]
    result = "".join(result)
    msg = "```\n" + result + "```"
    return update.effective_message.reply_text(msg, parse_mode="MARKDOWN")


SHOUT_HANDLER = DisableAbleCommandHandler("shout", shout)

dispatcher.add_handler(SHOUT_HANDLER)

__command_list__ = ["shout"]
__handlers__ = [SHOUT_HANDLER]
